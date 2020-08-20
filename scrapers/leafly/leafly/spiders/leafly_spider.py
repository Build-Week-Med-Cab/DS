import scrapy


class LeaflySpider(scrapy.Spider):
    name = "leafly"

    def start_requests(self):
        urls = [
            f'https://www.leafly.com/strains?sort=name&page={i}'
            for i in range(1, 116)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for strain_link in response.css('div.strain-playlist-grid a::attr(href)'):
            strain_link = response.urljoin(strain_link.get())
            yield scrapy.Request(strain_link, self.parse_strain)

    def parse_strain(self, response):
        strain = response.css('#strain-card-data > header > div.flex.flex-row.justify-between.items-center.border-t.border-deep-green-40.py-xs > div > h1').css('::text').get()
        aka = response.css('#strain-card-data > header > div.flex.flex-row.justify-between.items-center.border-t.border-deep-green-40.py-xs > div > h2').css('::text').get()
        if aka and aka.startswith('aka '):
            aka = aka[4:]
        type_ = response.css('#strain-card-data > header > div.flex.flex-row.justify-between.items-center.pb-xs > h2 > a').css('::text').get()
        rating = response.css('#strain-card-data > header > div.flex.flex-row.justify-between.items-center.pb-xs > div > p > span').css('::text').get()
        try:
            rating = float(rating.strip())
        except:
            rating = None
        num_reviews = response.css('#strain-card-data > header > div.flex.flex-row.justify-between.items-center.pb-xs > div > p > a').css('::text').get()
        try:
            num_reviews = int(num_reviews.split()[0])
        except:
            num_reviews = None
        description = response.css('#strain-description > div > p')
        try:
            description = ''.join(description.css('::text').getall())
        except:
            description = response.css('#strain-description > div > p').css('::text').get()
        num_effects_reports = response.css('#strain-effects-section > div.flex.items-center.font-mono.text-xs').css('::text').get()
        try:
            num_effects_reports = int(num_effects_reports.split()[0])
        except:
            num_effects_reports = None
        if num_effects_reports is not None:
            effects = response.css('#strain-effects-section > div.react-tabs.mt-lg > div > div')
        else:
            effects = None
        if effects and len(effects) == 3:
            feelings = self.parse_effects(effects[0])
            helps = self.parse_effects(effects[1])
            negative = self.parse_effects(effects[2])
        else:
            feelings = helps = negative = [(None, None)] * 5
        
        yield {
            'strain': strain,
            'aka': aka,
            'type': type_,
            'rating': rating,
            'num_reviews': num_reviews,
            'num_effects_reports': num_effects_reports,
            'feeling_1': feelings[0][0],
            'feeling_1_pct': feelings[0][1],
            'feeling_2': feelings[1][0],
            'feeling_2_pct': feelings[1][1],
            'feeling_3': feelings[2][0],
            'feeling_3_pct': feelings[2][1],
            'feeling_4': feelings[3][0],
            'feeling_4_pct': feelings[3][1],
            'feeling_5': feelings[4][0],
            'feeling_5_pct': feelings[4][1],
            'helps_1': helps[0][0],
            'helps_1_pct': helps[0][1],
            'helps_2': helps[1][0],
            'helps_2_pct': helps[1][1],
            'helps_3': helps[2][0],
            'helps_3_pct': helps[2][1],
            'helps_4': helps[3][0],
            'helps_4_pct': helps[3][1],
            'helps_5': helps[4][0],
            'helps_5_pct': helps[4][1],
            'negative_1': negative[0][0],
            'negative_1_pct': negative[0][1],
            'negative_2': negative[1][0],
            'negative_2_pct': negative[1][1],
            'negative_3': negative[2][0],
            'negative_3_pct': negative[2][1],
            'negative_4': negative[3][0],
            'negative_4_pct': negative[3][1],
            'negative_5': negative[4][0],
            'negative_5_pct': negative[4][1],
            'description': description,
            'url':response.url,
        }

    def parse_effects(self, sl:scrapy.selector.unified.SelectorList):
        texts = sl.css('::text').getall()
        effects = []
        for i in range(0, len(texts), 4):
            effects.append((texts[i], float(texts[i+2]) / 100))
        for i in range(5 - len(effects)):
            effects.append((None, None))
        return effects
