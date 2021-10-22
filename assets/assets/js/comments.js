$(document).on("click", ".comment_btn", function () {
    console.log(555)
    $.ajax({
        url: "/comment/",
        type: "post",
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        success: function (data) {
            console.log(data)
        }
    })
})