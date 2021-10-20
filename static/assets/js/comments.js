function get_comment_list() {
    $.ajax({
        url: "/query_comment_list/",
        type: "post",
        data: {
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
            "article_id": article_id,

        },
        success: function (data) {
            console.log(data)
            //情况评论框
            $("#comment_list").html(data.content_html)
        }
    })
}

$(document).ready(get_comment_list())

$(document).on("click", "#comment_btn", function () {

    var pid = ""
    var content = $("#comment_content").val()
    if (content) {

        $.ajax({
            url: "/comment/",
            type: "post",
            data: {
                "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
                "article_id": article_id,
                "content": content,
                "pid": pid,
            },
            success: function (data) {
                console.log(data)
                //情况评论框
                $("#comment_content").val("")
                get_comment_list()
            }
        })
    }

})