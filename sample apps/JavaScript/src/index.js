import './index.css';

import {getUsers, deleteUser} from './api/userApi';
import {wrap} from './common/execute_around_command';

function logInfo(message) {
  console.log(message);
  document.getElementById('log').innerHTML += '<br/>';
  document.getElementById('log').innerHTML += message;
}

// Populate table of users via API call.
getUsers().then(result => {
  wrap(logInfo)(() => {
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
