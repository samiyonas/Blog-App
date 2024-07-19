#!/usr/bin/node
// simple DOM manipulation for the profile page

$(document).ready(function() {
    $("button#new-content").on('click', function(event) {
        event.preventDefault();
        const title = $("input#post-title").val()
        const subtitle = $("input#post-subtitle").val()
        const content = $("textarea#post-content").val()

        const data = {
            "title": title,
            "subtitle": subtitle,
            "content": content
        }

        $.ajax({
            type: 'POST',
            url: '/home/post',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(data),
            encode: true,
            success: function(response) {
                alert('You posted!')
            },
            error: function(response) {
                alert('Something went wrong!')
            }
        })
    })
})

$(document).on('click', "div.see-more", function(event) {
    event.preventDefault();
    
    const title = $(this).find("h3.title-post").text();
    const subtitle = $(this).find("h4.subtitle-post").text();
    const content = $(this).find("p.content-post").text();

    const data = {
        "title": title,
        "subtitle": subtitle,
        "content": content
    };

    $.ajax({
        type: 'POST',
        url: '/home/reading_page',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        encode: true,
        success: function(response) {
            if (response.html) {
                $('body').html(response.html);
            }
        },
        error: function(response) {
            alert('Something went wrong!');
        }
    });
});

$(document).on('click', "button#update-btn", function(event) {
    event.preventDefault()

    const new_uname = $("input#username").val()
    const new_name = $("input#name").val()

    console.log(new_name);
    console.log(new_uname);

    const data = {
        "username": new_uname,
        "name": new_name
    }

    if (new_uname && new_name){
        $.ajax({
            type: 'PUT',
            url: '/home/update_user',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(data),
            encode: true
        })
    }
    else {
        alert("You have to update both username and name!");
    }
})
$(document).on('click', 'button.submit-comment', function(event){
    event.preventDefault()
    
    const content = $(this).closest('.post').find('textarea.comment-text').val();
    const post_id = $(this).closest('.post').data('id');

    const data = {
        "content": content,
        "post_id": post_id
    }

    if (content) {
        $.ajax({
            type: 'POST',
            url: '/home/comment',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(data),
            encode: true,
            success: function(response) {
                alert('You commented');
            },
            error: function(response) {
                alert('Something went wrong!')
            }
        })
    }
})