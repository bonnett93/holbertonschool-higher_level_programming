#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  }
  const tasks = {};
  for (let i = 1; i < 11; i++) {
    tasks[String(i)] = 0;
  }
  const jsonBody = JSON.parse(response.body);
  for (const task of jsonBody) {
    if (task.completed === true) {
      tasks[task.userId] += 1;
    }
  }
  for (const key in tasks) {
    if (tasks[key] === 0) {
      delete tasks[key];
    }
  }
  console.log(tasks);
});
