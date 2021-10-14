# -*- coding: utf-8 -*-

'''
几个实体：俱乐部(Club)、棋手(Player)、锦标赛(Tournament)、赞助商

根据需求建立关系数据表，如锦标赛-棋手之间的关系：赛程表（Match）

其中会员关系体现在Player表，即from字段
且该表增加两个字段,since_date(加入俱乐部的日期)、leave_date(离开俱乐部的日期). 
棋手转会时，插入一条新纪录since_date为当前日期，并更新上一条记录的leave_date为当前日期

也即拉链表的设计，保存历史会员转会快照 
如查询2018年的会员关系：select * from Player where since_date < '2019' and end_date >= '2018'

CREATE TABLE `Club` (
  `id` varchar(32) NOT NULL COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '名称',
  `location` varchar(100) COMMENT '地址',
  `update_time` int(16) DEFAULT 0 COMMENT '更新时间',
  `delete_time` int(16) DEFAULT 0 COMMENT '删除时间',
  `create_time` int(16) DEFAULT 0 COMMENT '创建时间',
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='俱乐部'


CREATE TABLE `Player` (
  `id` varchar(32) NOT NULL COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '名称',
  `location` varchar(100) COMMENT '地址',
  `from` varchar(32) COMMENT '来自的俱乐部id',
  `rank` int(10) COMMENT '排名',
  `since_date` varchar(32) DEFAULT '1970-01-01' COMMENT '加入俱乐部的日期'
  `leave_date` varchar(32) DEFAULT '9999-12-31' COMMENT '离开俱乐部的日期'
  `update_time` int(16) DEFAULT 0 COMMENT '更新时间',
  `delete_time` int(16) DEFAULT 0 COMMENT '删除时间',
  `create_time` int(16) DEFAULT 0 COMMENT '创建时间',
  PRIMARY KEY (`id`, `from`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='棋手'

CREATE TABLE `Tournament` (
  `id` varchar(32) NOT NULL COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '名称',
  `assit` varchar(500) COMMENT '赞助商',    # 多个赞助商以，分隔
  `since_date` varchar(32) COMMENT '开始日期',
  `end_date` varchar(32) COMMENT '结束日期',
  `update_time` int(16) DEFAULT 0 COMMENT '更新时间',
  `delete_time` int(16) DEFAULT 0 COMMENT '删除时间',
  `create_time` int(16) DEFAULT 0 COMMENT '创建时间',
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='锦标赛'

CREATE TABLE `Match` (
  `tour` varchar(100) COMMENT '锦标赛事id',
  `rounds` int(10) COMMENT `比赛轮次`,
  `date` varchar(32) COMMENT '比赛日期',
  `home` varchar(32) NOT NULL COMMENT '主队id',
  `away` varchar(32) NOT NULL COMMENT '客队id',
  `update_time` int(16) DEFAULT 0 COMMENT '更新时间',
  `delete_time` int(16) DEFAULT 0 COMMENT '删除时间',
  `create_time` int(16) DEFAULT 0 COMMENT '创建时间',
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='赛程'
'''