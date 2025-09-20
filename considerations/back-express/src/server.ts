import express = require("express");
import cors = require("cors");

const app: express.Application = express();
const port: number = 8081;

var corsOptions = {
  origin: "http://localhost:8080"
};

app.use(cors(corsOptions));
app.use(express.json()); // for parsing JSON
app.use(express.urlencoded({ extended: true })); // for parsing form data

// Handling '/' Request
app.get('/', (_req, _res) => {
  _res.send("TypeScript With Express");
});

require("./routes/HelloWorld.ts")(app);

// Server setup
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}/`);
});
