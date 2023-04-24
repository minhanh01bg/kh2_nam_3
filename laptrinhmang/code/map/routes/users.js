import express from "express";

import { createUser, getUsers, getUser, deleteUser, updateUser, testDatabase } from '../controllers/users.js';


const router = express.Router();
router.get('/', testDatabase)



// router.get('/', getUsers);

// //create
// router.post('/', createUser);

// router.get('/:id', getUser)

// //delete
// router.delete('/:id', deleteUser)

// //update
// router.patch('/:id', updateUser);

export default router;