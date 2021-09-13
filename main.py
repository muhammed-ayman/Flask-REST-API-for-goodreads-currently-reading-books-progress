from flask import Flask
from flask_restful import Api, Resource
from good_reads_progress_scraper import GoodReadsProgressScraper

app = Flask(__name__)
api = Api(app)

class DataHandler(Resource):
    def get(self, user_id):
        goodreads_inst = GoodReadsProgressScraper(user_id)
        goodreads_inst.scrape()
        return goodreads_inst.books_progress_percentages

api.add_resource(DataHandler, "/<int:user_id>")

if __name__ == '__main__':
    app.run(debug=True)
