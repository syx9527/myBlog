// 获取文章列表,网页加载完成后即运行
$(document).ready(function () {

    $.ajax({
        url: "/query_article_list/",
        type: "post",

        username: username,
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {
            if (data.code = 1) {
                $('#article_list').html(data.content_html);
            }

        }
    });

    $.ajax({
        url: "/query_tag_list/",
        type: "post",

        username: username,
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {
            if (data.code = 1) {
                $('#tag_list').html(data.content_html);
            }

        }
    });

    $.ajax({
        url: "/query_cate_list/",
        type: "post",

        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            if (data.code = 1) {
                $('#cate_list').html(data.content_html);
            }
        }
    });

    // 获取归档列表
    $.ajax({
        url: "/query_month_list/",
        type: "post",


        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {
            if (data.code = 1) {
                $('#year_month').html(data.content_html);
            }
        }
    });

});


// 触发点击事件，js渲染后点击失效，已经解决
$(document).on("click", ".author_btn", function () {
    var id = this.id;
    var name = this.getAttribute("name");
    console.log(id, name)
    $.ajax({
        url: "/query_article_list/",
        type: "post",


        data: {
            id: id,
            name: name,
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {
            if (data.code = 1) {
                $('#article_list').html(data.content_html);
            }
        }
    })
});