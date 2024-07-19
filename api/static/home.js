#!/usr/bin/node
// functionality to the posts

$(document).ready(function() {
    $("div.blog").click(function(event) {
        event.preventDefault();

        const title = $(this).find("h3.title").text()
        const subtitle = $(this).find("h4.subtitle").text()
        const content = $(this).find("p.content").text()

        const data = {
            "title": title,
            "subtitle": subtitle,
            "content": content
        }

        $.ajax({
            type: 'POST',
            url: '/home/reading_page',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(data),
            encode: true,
            success: function(response) {
                if (response.html){
                    $('body').html(response.html);
                }
            },
            error: function(response) {
                alert('Something went wrong!')
            }
        })
    })
})