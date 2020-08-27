# FastAPI app

Endpoint documentation:
- [https://medcabinet-ds-0820.herokuapp.com/](https://medcabinet-ds-0820.herokuapp.com/)
- [https://medcabinet-ds-0820.herokuapp.com/redoc](https://medcabinet-ds-0820.herokuapp.com/redoc)
- [OpenAPI JSON Specification](https://medcabinet-ds-0820.herokuapp.com/openapi.json)
for use in developer/testing tools like [Postman](https://www.postman.com)

Run locally:
- enter virtual environment: `pipenv shell`
- launch web server (in repo root): `uvicorn app.main:app --reload`

Deploy to Heroku using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):
- enter virtual environment: `pipenv shell`
- login to heroku: `heroku login`
- create app: `heroku create your-app-name-goes-here`
- create git remote: `heroku git:remote -a your-app-name-goes-here`
- deploy: `git push heroku <current_branch>:master`
