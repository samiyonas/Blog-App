#!/usr/bin/node
// Dom manipulation for the home page

$(document).ready(function() {
    $("a#signup").on("click", function(){
        $.ajax({
            type: 'GET',
            url: '/home/signup/',
        })
    })
})