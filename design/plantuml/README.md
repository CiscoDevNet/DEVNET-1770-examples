
- plantuml bot.txt

# Try adding

```
boundary ngrok
flask <- ngrok: webooks
flask -> Spark: GET /people/me
ngrok <-- SparkWebhook: JSON payload
flask -> Spark: POST /messages
ngrok <-- SparkWebhook: JSON Payload
```
