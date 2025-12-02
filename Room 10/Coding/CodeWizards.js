function filterUsers(users) {
  return users
    .filter(user => user.age >= 18)
    .map(user => user.name.toUpperCase());
}

const users = [
  { name: "alice", age: 17 },
  { name: "bob", age: 20 },
  { name: "carol", age: 25 }
];

console.log(filterUsers(users));
