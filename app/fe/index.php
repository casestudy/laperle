<?php

include "..\be\classes\User.php" ;

$user1 = new User() ;
$user2 = new User();

echo "
<h1>Add a new contact</h1>

<label for 'contact-name'> Contact </label >
<input name='contactname' value='' /> <br>
<label for 'phone-number'> Phone Number </label>
<input name= 'phone number' value='' placeholder='67589043'> <br>
    <button for 'submit' onclick='return addcontact()'> Submit </button>
    <script type='javascript' src='js/main.js'/>
";

