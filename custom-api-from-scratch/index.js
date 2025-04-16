const app = require('express')();
const port = 8080;

app.listen(
    port,
    () => console.log(`Listening to http://localhost:${port}`)
)

app.