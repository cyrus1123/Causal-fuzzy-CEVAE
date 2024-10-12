
import apache_beam as beam
from apache_beam.io.kafka import ReadFromKafka, WriteToKafka
from confluent_kafka import Producer, Consumer, KafkaError

class IngestFromKafka:
    def __init__(self, kafka_topic, bootstrap_servers):
        self.kafka_topic = kafka_topic
        self.bootstrap_servers = bootstrap_servers

    def create_pipeline(self):
        pipeline_options = beam.pipeline.PipelineOptions()
        with beam.Pipeline(options=pipeline_options) as p:
            kafka_data = (p
                          | 'ReadFromKafka' >> ReadFromKafka(consumer_config={'bootstrap.servers': self.bootstrap_servers},
                                                             topics=[self.kafka_topic])
                          )
            kafka_data | 'WriteToKafka' >> WriteToKafka(producer_config={'bootstrap.servers': self.bootstrap_servers},
                                                        topic=self.kafka_topic)
