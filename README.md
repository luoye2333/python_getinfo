# python_getinfo
get steam info(recommendations&amp;friends)
get recommendations:
gets info every 10 seconds
cause you cannot achieve all recommendations in one time
they are hided within the slide bar&cannot be achieved

get friends info:
level high to level low(depth first searching)
ending up in circular
because high level(lv=500+) players have similar friends

it is used to verify the theory that:
all people can be connected within 6 friends
i think it impossible though
because it needs a huge network to show relationships


to be improved
获取steam上的信息：
推荐游戏的信息是每隔10s获取一次
因为它会滚动播出，每次只能获得一个游戏的名称

获取好友信息：
以广度优先遍历每个人的好友列表（前6名）因为好友太多遍历不过来……
到最后会陷入死循环 因为高等级的大佬们喜欢互相加好友

用来验证六度理论的设想。
暂时无法完成，建立不了完整的图。

之后有空在改进：主要是提升效率，因为目前每次遍历加载网页要差不多3s
还要解决最后的死循环问题，就是遇到重复的人直接跳出。
