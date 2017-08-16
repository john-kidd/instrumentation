import './index.css';

import {getUsers, deleteUser} from './api/userApi';
import {logWrap, handleError} from './common/execute_around_command';
import {createContact} from './commands/create_contact';

function logInfo(message) {
  console.log(message);
  document.getElementById('log').innerHTML += '<br/>';
  document.getElementById('log').innerHTML += message;
}

function logError(message) {
  console.error(message);
  document.getElementById('error').innerHTML += '<br/>';
  document.getElementById('error').innerHTML += message;
}

// Populate table of users via API call.
getUsers().then(result => {
  logWrap(logInfo)(() => {
    let usersBody = "";

    result.forEach(user => {
      usersBody+= `<tr>
        <td><a href="#" data-id="${user.id}" class="deleteUser">Delete</a></td>
        <td>${user.id}</td>
        <td>${user.firstName}</td>
        <td>${user.lastName}</td>
        <td>${user.email}</td>
        </tr>`
    });

    global.document.getElementById('users').innerHTML = usersBody;

    const deleteLinks = global.document.getElementsByClassName('deleteUser');

    // Must use array.from to create a real array from a DOM collection
    // getElementsByClassname only returns an "array like" object
    Array.from(deleteLinks, link => {
      link.onclick = function(event) {
        const element = event.target;
        event.preventDefault();
        deleteUser(element.attributes["data-id"].value);
        const row = element.parentNode.parentNode;
        row.parentNode.removeChild(row);
      };
    });
  }, () => 'getUsers');
});

function divide(x, y) {
  if (x === 0 || y === 0)
    throw new Error('divide by zero error');
  return x / y;
}

function createNewContact() {
  const contact = { id: 1, name: 'John Kidd' };
  createContact(logInfo, 'create contact')(contact);
}

try {
  const execute = handleError(logError, logInfo);

  execute(createNewContact, () => 'create contact');
  execute(() => divide(1, 0), () => 'divide');
} catch(ex) {
  logError(ex);
}

createContact(logInfo)