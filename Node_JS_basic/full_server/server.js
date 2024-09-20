import express from 'express';
import routes from './routes/index.js';

const app = express();
const PORT = 1245;

app.use(express.json());
app.use(routes);

export default app;

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
  });
}
