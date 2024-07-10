#!/usr/bin/node
// to handle what happens when sign up button is clicked

$(document).ready(function() {
    $("#signup-form").on("submit", function(event) {
        event.preventDefault(); //prevent the default form submission which is 'GET'
        let data = {
            "name": $("input#name").val(),
            "username": $("input#username").val(),
            "email": $("input#email").val(),
            "password": $("input#password").val()
        }

        console.log(data);

        $.ajax({
            type: 'post',
            url: '/home/signup',
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            encode: true,
            success: function(response) {
                alert(`Hey ${data.name}, You've successfully signed up!`);
            },
            error: function(response) {
                console.log("Error:", response);
                alert(`Sorry ${data.name}, Something went wrong`);
            }
        })
    })
})