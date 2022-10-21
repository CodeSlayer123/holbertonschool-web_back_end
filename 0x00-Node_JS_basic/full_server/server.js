const express = require("express");
const port = 1245;
const routes = require('./routes/index');

const app = express();

app.use(routes)

app.listen(port);

export default app;