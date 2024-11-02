# Wait for the Kafka broker to start
sleep 10

# Create topics
kafka-topics.sh --create --topic crypto_quote --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic crypto_market --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1