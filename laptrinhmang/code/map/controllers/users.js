import { v4 as uuidv4 } from 'uuid';
import { con } from '../database.js'
// const db = require('../database')
// import
let users = [];
// const mysql = require('mysql');
export const getUsers = (req, res) => {
    console.log(users);
    res.send(users);
}

export const createUser = (req, res) => {
    const user = req.body;
    users.push({...user, id: uuidv4() });
    res.send(`User with the username ${user.name} added to the database`);
}

export const getUser = (req, res) => {
    const id = req.params.id;

    const foundUser = users.find((user) => user.id === id);

    res.send(foundUser);
}

export const deleteUser = (req, res) => {
    const { id } = req.params;
    users = users.filter((user) => user.id !== id);

    res.send(`user with the id ${id} delete from the database`);
}

export const updateUser = (req, res) => {
    const { id } = req.params;
    const { name, lastName, age } = req.body;
    const user = users.find((user) => user.id === id);
    if (name)
        user.name = name;

    if (lastName)
        user.lastName = lastName;

    if (age)
        user.age = age;
    res.send(`User with the id ${id} has been updated`)

}

export const testDatabase = (req, res) => {
    try {
        con.connect((err) => {
            console.log("connected");
            if (err) throw err;
            con.query(`select * from vehicle`, (err, result, fields) => {
                if (err) throw err;
                console.log(result);
                res.send(result)
            });
        });
    } catch (err) {
        console.log(err);
    }
};