<h1>Smart Park</h1>
<i><h3 style="margin-top: -20px;margin-bottom: 15px;">Your frineds for renting a park</h3></i>
With <b>Smart Park</b> you can offer your private parking for any time and price you choose <i>or</i> you can rent a private park near your work.
<br>
<br>
<ul>
    <li> <mark><b>&nbsp;As Owner&nbsp;</b></mark>
    <ol>
        <li>Download our App <a href="https://github.com/Elbargho/Smart-Park/tree/main/Smart%20Park%20App">here</a> and sign-up as owner</li>
        <li>Add your park providing its location, starting/ending time and price/h</li>
        <li>Place a device connected to a camera in your park</li>
        <li>Using the device, login to our Camera App <a href="https://cameraappiot.azurewebsites.net/">here</a>
    </ol>
    </li><br>
    <li> <mark><b>&nbsp;As Tenant&nbsp;</b></mark>
        <ol>
            <li>Download our App <a href="https://github.com/Elbargho/Smart-Park/tree/main/Smart%20Park%20App">here</a> and sign-up as tenant</li>
            <li>Pick your desired parking from the <i>Parks Table</i> section
        </ol>
    </li>
</ul>
<br>

<u><a href="#sec1">General App features and functions</a><br></u>
<u><a href="#sec2">Owner features and functions</a><br></u>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u><a href="#sec21">Owner SignalR</a><br></u>
<u><a href="#sec3">Tenant features and functions</a><br></u>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u><a href="#sec31">Tenant SignalR</a><br></u>
<u><a href="#sec4">Camera App features and functions</a><br>
<a href="#sec5">Storage tables</a></u><br>
<a href="#sec6">Demo videos</a></u>

<br><br>
<div id="sec1">
<small><h1>General App features and functions</h1></small>
<ul>
    <b><li>Login</b> (Username, Password)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/usersignin">Code</a>&nbsp;&nbsp;&nbsp;Queries&nbsp;&nbsp;&nbsp;<a href="#accounts_table">Accounts Table</a><br>
    <b><li>Sign Up</b> (Username, Password, Credit Card, Plate Number, Account Type)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/addnewuser">Code</a>&nbsp;&nbsp;&nbsp;Adds Entry to&nbsp;&nbsp;&nbsp;<a href="#accounts_table">Accounts Table</a>
    <i>Note: Checks that username doesn't already exist</i>
    <b><li>My Profile</b> (Username, Password)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/usersignin">Code</a>&nbsp;&nbsp;&nbsp;Queries&nbsp;&nbsp;&nbsp;<a href="#accounts_table">Accounts Table</a>
    <b><li>Update Profile</b> (Username, Old Password, New Password, Credit Card, Plate Number)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/updateUser">Code</a>&nbsp;&nbsp;&nbsp;Updates Entity in&nbsp;&nbsp;&nbsp;<a href="#accounts_table">Accounts Table</a>
</ul>
<div style="display: flex; justify-content: space-evenly; margin-top: 25px;">
<img src="https://i.ibb.co/D1gvfv6/Main-Activity.png" style="width: 30%;"/>
<img src="https://i.ibb.co/fxj6kF2/Sign-Up-Activity.png" style="width: 30%;"/>
<img src="https://i.ibb.co/PDtKNmF/Owner-Profile-Activity.png" style="width: 30%;"/>
</div>
</div>
<br><br>
<div id="sec2">
<small><h1>Owner features and functions</h1></small>
<ul>
    <b><li id="add_park">Add Park</b> (Username, Password, Location, Start-time, End-time, Price/h)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/addPark">Code</a>&nbsp;&nbsp;&nbsp;Adds Entry to&nbsp;&nbsp;&nbsp;<a href="#parks_table">Parks Table</a>
    <b><li>Remove Park</b> (Username, Password, Location) </li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/removePark">Code</a>&nbsp;&nbsp;&nbsp;Removes Entry from&nbsp;&nbsp;&nbsp;<a href="#parks_table">Parks Table</a>
</ul>
<div style="display: flex; justify-content: space-evenly; margin-top: 25px;">
<img src="https://i.ibb.co/bmhjWfN/Owner-Activity.png" style="width: 30%;"/>
<img src="https://i.ibb.co/GQ647NM/Add-Park-Activity.png" style="width: 30%;"/>
</div>
</div>
<br><br>
<div id="sec21">
<small><h1>Owner SignalR</h1></small>
<ul>
    <b><li>Show Budget</b> Shows the owner budget when the reserver leaves the park</li> Triggered by&nbsp;&nbsp;&nbsp;<a href="#release_park">Release Park</a>
    <b><li>Park Reserved</b> Sends notification when a user reserves the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#reserve_park">Reserve Park</a>
    <b><li>Reserver Entered</b> Sends notification when the reserver enters the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#reserver_entrance">Reserver Entrance</a>
    <b><li>Stranger Entered</b> Sends notification when a stranger enters the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#stranger_entrance">Stranger Entrance</a>
    <b><li>Car Left</b> Sends notification when a user leaves the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#user_leaves">User Leaves</a>
    <b><li>Tenant hit half hour limit</b> Sends notification when the park has less than half hour left and the tenant is still in the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#time_limit">Time Limit</a>
</ul>
</div>
<br><br>
<div id="sec3">
<small><h1>Tenant features and functions</h1></small>
<ul>
    <b><li>Show Parks</b> </li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/getParksTable">Code</a>&nbsp;&nbsp;&nbsp;Queries <a href="#parks_table">Parks Table</a><br>
    <i>Note: Shows only available parks</i>
    <b><li id="reserve_park">Reserve Park</b> (Username, Password, Location)</li> <a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/reservePark">Code</a>&nbsp;&nbsp;&nbsp;Updates <a href="#parks_table">Parks Table</a>&nbsp;&nbsp;&nbsp;Adds entity to <a href="#requests_table">Requests</a>
</ul>
<div style="display: flex; justify-content: space-evenly; margin-top: 25px;">
<img src="https://i.ibb.co/y6QH9fs/Tenant-Activity.png" style="width: 30%;"/>
<img src="https://i.ibb.co/f9NXg2h/Show-Available-Parks-And-Reserve.png" style="width: 30%;"/>
</div>
</div>
<br><br>
<div id="sec31">
<small><h1>Tenant SignalR</h1></small>
<ul>
    <b><li>Parks Table updated</b> Updates parks table when a park is added</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#add_park">Add Park</a>
    <b><li>Show Cumulitive Bill</b> Shows the tenant current cumulative bill</li> Triggered by&nbsp;&nbsp;&nbsp;<a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/getCurrentPayment">Get Current Payment</a>
    <b><li>Total Bill On Exit</b> Sends notification with bill when the tenant exits the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#user_leaves">User Leaves</a>
    <b><li>Tenant hit half hour limit</b> Sends notification when the park has less than half hour left and the tenant is still in the park</li>Triggered by&nbsp;&nbsp;&nbsp;<a href="#time_limit">Time Limit</a>
</ul>
</div>
<br><br>
<div id="sec4">
<small><h1>Camera App features and functions</h1></small>
<ul>
    <b><li id="reserver_entrance">Reserver Entered</b> Detects a reserver entering the park</li>Queries&nbsp;&nbsp;&nbsp;<a href="#requests_table">Requests Table</a>
    <b><li id="stranger_entrance">Stranger Entered</b> Detects a stranger entering the park</li>Queries&nbsp;&nbsp;&nbsp;<a href="#requests_table">Requests Table</a>
    <b><li id="user_leaves">Car Left</b> Detects a car leaving the park</li>Calls&nbsp;&nbsp;&nbsp;<a href="#release_park">Release Park</a>&nbsp;&nbsp;&nbsp;if the car belongs to the reserver
    <b><li id="release_park">Release Park</b> Releases the park thus billing the tenant and marking the park as not full</li><a href="https://github.com/Elbargho/Smart-Park/tree/main/Azure%20FunctionApps/releasePark">Code</a>&nbsp;&nbsp;&nbsp;Deletes from <a href="#requests_table">Requests Table</a>&nbsp;&nbsp;&nbsp;Updates<a href="#parks_table"> Parks Table</a>
    <b><li id="time_limit">Time Limitation</b> Detects that the park has less than half hour left and the tenant is still in the park</li>Queries&nbsp;&nbsp;&nbsp;<a href="#parks_table">Parks Table</a>
</ul>
<div style="display: flex; justify-content: space-evenly; margin-top: 25px;">
<img src="https://i.ibb.co/rxS41g5/c1084398-48e3-428d-9ce0-57a3f0c719fd.jpg" style="width: 30%;"/>
<img src="https://i.ibb.co/tHywdJ5/Whats-App-Image-2022-08-15-at-7-11-03-PM.jpg" style="width: 30%;"/>
<img src="https://i.ibb.co/BT5gzWn/Enter-The-Park-Witout-Reservation.jpg" style="width: 30%;"/>
</div>
<div style="display: flex; justify-content: space-evenly; margin-top: 25px;">
<img src="https://i.ibb.co/3hfQT4p/Thre-Reserver-Enter-The-Park.jpg" style="width: 30%;"/>
<img src="https://i.ibb.co/cDNJpHH/Whats-App-Image-2022-08-15-at-7-09-03-PM.jpg" style="width: 30%;"/>
<img src="https://i.ibb.co/ssz3zRw/Car-Is-Left.jpg" style="width: 30%;"/>
</div>
</div>
<br><br>
<div id="sec5">
<small><h1>Storage tables</h1></small>
<ul>
    <b><li id="accounts_table">Accounts</b> (Username <b>Key</b>, Password <b>HASHED</b>, Account Type, Plate Number, Credit Card <b>HASHED</b>, Credit Card Last 4 Degits)
    <img src="https://i.ibb.co/cY2vnxq/acc.png" style="margin: 25px 0px;"/></li>
    <b><li id="parks_table">Parks</b> (Username <b>Key</b>, Location <b>Key</b>, Price/h, Start Time, End Time, Is Full)
    <img src="https://i.ibb.co/fn2drfw/parks.png" style="margin: 25px 0px;"/></li>
    <b><li id="requests_table">Requests</b> (Username <b>Key</b>, Location <b>Key</b>, Plate Number, Request Date)
    <img src="https://i.ibb.co/1JMm6hm/requests.png" style="margin: 25px 0px;"/></li>
</ul>
</div>
<br><br>
<div id="sec6">
<ul>
    <small><h1>Demo videos</h1></small>
    <b><li>Application features:</b> <a href="https://streamable.com/kz5hzv">link</a></li>
    <b><li>Park reservation features:</b> <a href="https://streamable.com/ppfc2z">link</a></li>
    <b><li>Half hour limitation:</b> <a href="https://streamable.com/3w3e0n">link</a></li>
</ul>
</div>