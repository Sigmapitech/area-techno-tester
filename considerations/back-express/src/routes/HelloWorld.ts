import { Express, Request, Response, Router } from 'express';

const HelloWorldRoute = (app: Express) => {
  const router: Router = Router();

  router.get("/", (req: Request, res: Response) => {
    res.send({ message: "Hello World!" });
  });

  app.use('/api/', router);
};

export default HelloWorldRoute;
module.exports = HelloWorldRoute;
