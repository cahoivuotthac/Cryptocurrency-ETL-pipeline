curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" http://localhost:8083/connectors/ -d '{
    "name": "cryptocurrency_connector",
    "config": {
        "connector.class": "io.debezium.connector.mysql.MySqlConnector",
        "database.hostname": "mysql",
        "database.port": "3306",
        "database.user": "debezium",
        "database.password": "dbz",
        "database.server.id": "184054",
        "topic.prefix": "dbserver1",
        "database.include.list": "cryptocurrency",
        "schema.history.internal.kafka.bootstrap.servers": "kafka:9092",
        "schema.history.internal.kafka.topic": "schema-changes.cryptocurrency",
        "table.include.list": "cryptocurrency.Cryptocurrency_Metrics, cryptocurrency.Cryptocurrency_USD_Quote, cryptocurrency.Global_Market, cryptocurrency.Global_Market_Dominances"
    }
}'
