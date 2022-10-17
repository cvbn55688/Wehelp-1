# 第五周作業
### 要求三
* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
  ```
  insert member(name, username, password, follower_count) values('Zhi_Han', 'test', 'test', 500);
  insert member(name, username, password, follower_count) values('name2', 'test2', 'test2', 345);
  insert member(name, username, password, follower_count) values('name3', 'test3', 'test3', 345);
  insert member(name, username, password, follower_count) values('name4', 'test4', 'test4', 567);
  insert member(name, username, password, follower_count) values('name5', 'test5', 'test5', 567);
  insert member(name, username, password, follower_count) values('name6', 'test6', 'test6', 567);
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196142444-c0321e58-f9ba-4a67-aea7-1fdbd106e2e5.png)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
  ```
  select * from member;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196142949-633fc78d-29c1-4e88-b1b9-599d02800d7f.png)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
  ```
  select * from member order by time desc;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196143336-a9e4944b-10be-411d-bfac-a6895c6ea4b2.png)

* 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
  ```
  select * from member order by time desc limit 1, 4;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196143597-c873f9b2-209e-4be2-9029-baca722228a9.png)

*  使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
  ```
  select * from member where username = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196144199-2b1ff295-d5f0-4d90-9922-5b5d61e2db1f.png)
