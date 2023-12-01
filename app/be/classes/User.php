<?php 
    class User {
        private $id;
        public $username;
        private $password;
        private $phonenumber;

        public function login() {
                return "<h1>I am {$this->username} I have logged in and my phone number is {$this->phonenumber}</h1>";
        }

        public function setUser($uname, $pass, $phone) {
            $this->username = $uname;
            $this->password = $pass;
            $this->phonenumber = $phone;
        }
    }


?>