//var label= document.createElement("label");
//var description = document.createTextNode(pair);
//var checkbox = document.createElement("input");

//checkbox.type = "checkbox";    // make the element a checkbox
//checkbox.name = "slct[]";      // give it a name we can check on the server side
//checkbox.value = pair;         // make its value "pair"

//label.appendChild(checkbox);   // add the box to the element
//label.appendChild(description);// add the description to the element

// add the label element to your div
//document.getElementById('list').appendChild(label);
var clientId = 'client';
var apiKey = 'jTWy6Utn`ouoZ3a';
var scopes = 'profile email https://www.googleapis.com/auth/drive.readonly';

var signinButton = document.getElementById('signin-button');
var signoutButton = document.getElementById('signout-button');

function initAuth() {
  gapi.client.setApiKey(apiKey);
  gapi.auth2.init({
      client_id: clientId,
      scope: scopes
  }).then(function () {
    // Listen for sign-in state changes.
    gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

    // Handle the initial sign-in state.
    updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());

    signinButton.addEventListener("click", handleSigninClick);
    signoutButton.addEventListener("click", handleSignoutClick);
  });
}

function updateSigninStatus(isSignedIn) {
  if (isSignedIn) {
    signinButton.style.display = 'none';
    signoutButton.style.display = 'block';
    makeApiCall();
  } else {
    signinButton.style.display = 'block';
    signoutButton.style.display = 'none';
  }
}

function handleSigninClick(event) {
  gapi.auth2.getAuthInstance().signIn();
}

function handleSignoutClick(event) {
  gapi.auth2.getAuthInstance().signOut();
}

// Load the API client and auth library
gapi.load('client:auth2', initAuth);




// $('#list').on('click', '.complete-button', function(event) {
//   var item = $(event.target).parent()
//   var isItemCompleted = item.hasClass('completed')
//   var itemId = item.attr('data-id')

//   var updateRequest = $.ajax({
//     type: 'PUT',
//     url: "/bucketlist" + itemId,
//     data: { completed: !isItemCompleted }
//   })

//   updateRequest.done(function(itemData) {
//     if (itemData.completed) {
//       item.addClass('completed')
//     } else {
//       item.removeClass('completed')
//     }
//   })

