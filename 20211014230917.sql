
INSERT INTO `my_blog`.`blog_article2tag` (`nid`, `article_id`, `tag_id`)
VALUES (2, 1, 1),
       (1, 2, 1),
       (3, 3, 2);
INSERT INTO `my_blog`.`blog_article` (`nid`, `title`, `desc`, `create_time`, `content`, `category`, `user`,
                                      `comment_count`, `down_count`, `up_count`)
VALUES (1, 'SpringBoot如何实现定时任务',
        'SpringBoot创建定时任务的方式很简单，主要有两种方式：一、基于注解的方式（@Scheduled）二、数据库动态配置。实际开发中，第一种需要在代码中写死表达式，如果修改起来，又得重启会显示很麻烦；所以我们往往会采取第二种方式，可以直接从数据库中读取定时任务的指定执行时间，无需重启。 ...',
        '2021-09-13 11:17:49.972000',
        'SpringBoot创建定时任务的方式很简单，主要有两种方式：一、基于注解的方式（@Scheduled）二、数据库动态配置。实际开发中，第一种需要在代码中写死表达式，如果修改起来，又得重启会显示很麻烦；所以我们往往会采取第二种方式，可以直接从数据库中读取定时任务的指定执行时间，无需重启。\r\n\r\n \r\n\r\n下面就来介绍下这两种方式吧\r\n\r\n一、基于注解（@Scheduled）\r\n基于注解是一种静态的方式，只需要几行代码就可以搞定了\r\n\r\n添加一个配置类',
        1, 2, 0, 0, 0),
       (2, 'Redis 起步',
        '由四个可执行文件：redis-benchmark、redis-cli、redis-server、redis-stat 这四个文件，加上一个redis.conf就构成了整...conf就构成了整个redis的最终可用包。它们的作用如下： redis-server：Redis服务器的daemon启动程序 redis-cli：Redis命令行操作工具。当',
        '2021-10-13 11:18:54.914399',
        'Redis是一个key-value存储系统。和Memcached类似，但是解决了断电后数据完全丢失的情况，而且她支持更多无化的value类型，除了和string外，还支持lists（链表）、sets（集合）和zsets（有序集合）几种数据类型。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。\r\n\r\n2.Redis的性能\r\n下面是官方的bench-mark数据：\r\n\r\nThe test was done with 50 simultaneous clients performing 100000 requests.\r\nThe value SET and GET is a 256 bytes string.\r\nThe Linux box is running Linux 2.6, it’s Xeon X3320 2.5Ghz.\r\nText executed using the loopback interface (127.0.0.1).\r\nResults: about 110000 SETs per second, about 81000 GETs per second.\r\n\r\n更多详细数据请见官方bench-mark page（http://code.google.com/p/redis/wiki/Benchmarks）',
        2, 2, 0, 0, 0),
       (3, 'MySQL函数',
        'GET_LOCK(\'MySQL\',10) ->1 (持续10秒) SELECT IS_FREE_LOCK(\'MySQL\') ->1 SELECT RELEASE_LOCK(\'MySQL\')... MySQL数据库提供了很多函数包括： 数学函数； 字符串函数； 日期和时间函数； 条件判断函数； 系统信息函数； 加密函数； 格式化函数； 一、数学函数',
        '2021-10-13 11:20:05.499425',
        'MySQL函数\r\n　　MySQL数据库提供了很多函数包括：\r\n\r\n数学函数；\r\n字符串函数；\r\n日期和时间函数；\r\n条件判断函数；\r\n系统信息函数；\r\n加密函数；\r\n格式化函数；\r\n一、数学函数',
        3, 2, 0, 0, 0);
INSERT INTO `my_blog`.`blog_blog` (`nid`, `title`, `site_name`, `theme`)
VALUES (1, '测试员的博客', 'cs', '测试'),
       (2, '小邵的个人博客', 'xiaoshao', '随心');
INSERT INTO `my_blog`.`blog_category` (`nid`, `title`, `blog`)
VALUES (1, 'SpringBoot', 1),
       (2, '数据库', 1),
       (3, '数据库x', 1);
INSERT INTO `my_blog`.`blog_tag` (`nid`, `title`, `blog_nid`)
VALUES (1, '测试标签', 1),
       (2, '测试标签2', 1);
INSERT INTO `my_blog`.`blog_userinfo` (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`,
                                       `email`, `is_staff`, `is_active`, `date_joined`, `nid`, `telephone`, `avatar`,
                                       `create_time`, `blog_id`)
VALUES ('pbkdf2_sha256$260000$0zrVrfYLEWKhTr1MBDHsS2$ACnFAPAJJolfzuxXuR3aUdbKq4DAbRnv4ILl1iD21eM=',
        '2021-10-14 20:05:39.160344', 1, 'syx', '', '', '1275241305@qq.com', 1, 1, '2021-10-12 12:47:00.000000', 1,
        '17606927841', 'avatars/lufei.jpg', '2021-10-12 12:47:47.099900', 2),
       ('pbkdf2_sha256$260000$RdWrBHczQpErXUfWsjY3Ue$rUOIUnOpeLuh4DwX7dgfdCGbGHNHq1cDoeLaP9G11mk=', NULL, 0, 'admin',
        '', '', 'admin@admin.com', 0, 1, '2021-10-13 11:12:00.000000', 2, 'ceshi', 'avatars/default_avatar_svx8J44.png',
        '2021-10-13 11:12:57.173471', 1);
INSERT INTO `my_blog`.`django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`,
                                          `change_message`, `content_type_id`, `user_id`)
VALUES (1, '2021-10-13 11:14:17.481748', '1', '测试员的博客', 1, '[{\"added\": {}}]', 8, 1),
       (2, '2021-10-13 11:14:36.718316', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Telephone\", \"Blog\"]}}]', 6,
        1),
       (3, '2021-10-13 11:15:52.546435', '2', '小邵的个人博客', 1, '[{\"added\": {}}]', 8, 1),
       (4, '2021-10-13 11:16:27.614644', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Telephone\"]}}]', 6, 1),
       (5, '2021-10-13 11:16:38.521359', '1', 'syx', 2,
        '[{\"changed\": {\"fields\": [\"Last login\", \"Telephone\", \"Blog\"]}}]', 6, 1),
       (6, '2021-10-13 11:17:31.082441', '1', 'SpringBoot', 1, '[{\"added\": {}}]', 11, 1),
       (7, '2021-10-13 11:17:49.973323', '1', 'SpringBoot如何实现定时任务', 1, '[{\"added\": {}}]', 7, 1),
       (8, '2021-10-13 11:18:34.511085', '2', '数据库', 1, '[{\"added\": {}}]', 11, 1),
       (9, '2021-10-13 11:18:54.916394', '2', 'Redis 起步', 1, '[{\"added\": {}}]', 7, 1),
       (10, '2021-10-13 11:19:36.705034', '3', '数据库', 1, '[{\"added\": {}}]', 11, 1),
       (11, '2021-10-13 11:20:05.500423', '3', 'MySQL函数', 1, '[{\"added\": {}}]', 7, 1),
       (12, '2021-10-13 11:20:24.103683', '3', '数据库x', 2,
        '[{\"changed\": {\"fields\": [\"\\u5206\\u7c7b\\u6807\\u9898\"]}}]', 11, 1),
       (13, '2021-10-13 11:20:29.985955', '3', 'MySQL函数', 2, '[]', 7, 1),
       (14, '2021-10-13 11:39:40.975617', '1', 'syx', 2, '[{\"changed\": {\"fields\": [\"Avatar\"]}}]', 6, 1),
       (15, '2021-10-13 13:53:02.306269', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Avatar\"]}}]', 6, 1),
       (16, '2021-10-13 15:01:08.543546', '1', '测试标签', 1, '[{\"added\": {}}]', 9, 1),
       (17, '2021-10-13 15:01:35.947246', '3', 'MySQL函数', 2, '[]', 7, 1),
       (18, '2021-10-13 15:02:05.642813', '1', 'Redis 起步---测试标签', 1, '[{\"added\": {}}]', 12, 1),
       (19, '2021-10-13 15:02:17.713526', '2', 'SpringBoot如何实现定时任务---测试标签', 1, '[{\"added\": {}}]', 12, 1),
       (20, '2021-10-13 15:02:18.708864', '2', 'SpringBoot如何实现定时任务---测试标签', 2, '[]', 12, 1),
       (21, '2021-10-13 15:04:44.640642', '2', '测试标签2', 1, '[{\"added\": {}}]', 9, 1),
       (22, '2021-10-14 22:23:15.597007', '3', 'MySQL函数', 2, '[{\"changed\": {\"fields\": [\"\\u4f5c\\u8005\"]}}]', 7,
        1),
       (23, '2021-10-14 22:23:30.016438', '2', '测试标签2', 2, '[]', 9, 1),
       (24, '2021-10-14 22:23:46.869359', '3', 'MySQL函数', 2, '[]', 7, 1),
       (25, '2021-10-14 22:24:23.249049', '3', 'MySQL函数---测试标签2', 1, '[{\"added\": {}}]', 12, 1),
       (26, '2021-10-14 22:34:40.858037', '3', '数据库x', 2,
        '[{\"changed\": {\"fields\": [\"\\u6240\\u5c5e\\u535a\\u5ba2\"]}}]', 11, 1);
