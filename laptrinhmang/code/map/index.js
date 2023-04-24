import express from 'express';
import usersRoutes from './routes/users.js';
// import dotenv from 'dotenv';

// dotenv.config();

const app = express();

const PORT = 5000;
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use('/users', usersRoutes);


app.get('/', (req, res) => {
    console.log("[test]!");
    res.send("hello from homepage");
});

try {
    app.listen(PORT, () => console.log(`server running on port: http://localhost:${PORT}`));
} catch (err) {
    console.log(err)
}