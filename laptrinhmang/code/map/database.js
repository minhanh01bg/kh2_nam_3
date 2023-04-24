import mysql from 'mysql2'
export let con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'fancy200',
    database: 'data_map'
})