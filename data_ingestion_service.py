
from fastapi import FastAPI
import apache_beam as beam

class DataIngestionService:
    def __init__(self):
        self.app = FastAPI()
        self.kafka_topic = "my_topic"
        self.bootstrap_servers = "localhost:9092"

    def setup_routes(self):
        @self.app.post("/ingest")
        async def ingest_data():
            self.create_pipeline()
            return {"status": "Data ingestion started"}

    def create_pipeline(self):
        pipeline_options = beam.pipeline.PipelineOptions()
        with beam.Pipeline(options=pipeline_options) as p:
            kafka_data = (p
                          | 'ReadFromKafka' >> beam.io.ReadFromKafka(
                              consumer_config={'bootstrap.servers': self.bootstrap_servers},
                              topics=[self.kafka_topic]
                          ))
            kafka_data | 'ProcessData' >> beam.Map(self.process_data)
    
    def process_data(self, data):
        # Send data for preprocessing
        requests.post("http://preprocessing-service:8000/preprocess", json={"data": data})

data_ingestion_service = DataIngestionService()
app = data_ingestion_service.app
