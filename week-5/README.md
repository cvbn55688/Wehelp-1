# 第五周作業

### 要求二
  ![image](https://user-images.githubusercontent.com/109027415/196150818-a30161be-7f42-4dce-a5f3-1fe9cce844c0.png)

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
    ![image](https://user-images.githubusercontent.com/109027415/196150159-a8b70262-bfb1-40ca-b9e1-359b64a8cbb6.png)

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
  select * from member order by time desc limit 1, 3;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196145511-33dc3b1c-e459-4047-a7e8-cc9ea25e90b3.png)

*  使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
  ```
  select * from member where username = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196144199-2b1ff295-d5f0-4d90-9922-5b5d61e2db1f.png)

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
  ```
  select * from member where username = 'test' and password = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196144530-a533f1b2-daff-4945-a937-cdf44cd1ec2f.png)
 
* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
  ```
    update member set username = 'test2' where username = 'test';
    select * from member where username = 'test2';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196145075-c4fb902a-ebf7-4cb7-91f9-0a1587d28aba.png)

### 要求四
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
  ```
  select count(id) from member;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196145962-9be40d9a-c481-492d-8091-00a652675a07.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
  ```
  select sum(follower_count) from member;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196146157-78623309-aed6-48ad-b3ab-aa07406899a1.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
  ```
  select avg(follower_count) from member;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196146289-b50800b2-4ed2-4069-8ea3-6a7120aeba20.png)
 
 ### 要求五
* 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。
  ![image](https://user-images.githubusercontent.com/109027415/196146629-0a593a3c-b5cc-4416-8386-b5a742e0265e.png)

* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
  ```
  select member.name, message.content from member inner join message on member.id = member_id;
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196147320-09d2176a-1018-4a40-9f81-02c174cd77f1.png)
  
* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
  ```
  select member.name, message.content from member inner join message on member.id = member_id where username = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196147922-d636ff0c-f8ef-4a25-afd7-21b97f881a68.png)

* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
  ```
  select avg(like_count) from message inner join member on member.id = member_id where username = 'test';
  ```
  ![image](https://user-images.githubusercontent.com/109027415/196148333-580b3ee7-8233-4914-af5d-1f927521b648.png)

### 輸出
  用CMD到mysqldump位置並輸入：
    ```
    mysqldump -u root -p website > data.sql
    ```


### 額外要求
* 創立一個likeCount table：

    ![image](https://user-images.githubusercontent.com/109027415/196439872-ca8ae27a-4540-4e4c-8c49-88e8e1b5f744.png)
    
  insert資料：
  
    ![image](https://user-images.githubusercontent.com/109027415/196439951-7bcc937d-34c5-4906-958d-295ae136bb3e.png)

* 可以根據留言編號取得該留言有哪些會員按讚。
  ```
  select member.name, message.content, likeCount.mess_id, likeCount.who_like from message 
  inner join likeCount on message.id = likeCount.mess_id 
  inner join member on member.id = message.member_id;
  ```
    ![image](https://user-images.githubusercontent.com/109027415/196439047-e7e2154b-0c7d-4d0d-8d17-f8a1b03a3222.png)
 
* 會員若是嘗試對留言按讚：要能先檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。
  ```
  insert likeCount(mess_id, who_like) select 3, 'name6' 
  where not exists(select * from likeCount where mess_id = 3 and who_like = 'name6');
  #因為'name6'已經對mess_id = 3點過讚了，所以insert並無作用。
  
  insert likeCount(mess_id, who_like) select 6, 'name6' 
  where not exists(select * from likeCount where mess_id = 6 and who_like = 'name6');
  #因為'name6'尚未對mess_id = 6點過讚，所以insert起作用。
  ```
    ![未命名](https://user-images.githubusercontent.com/109027415/196443650-ddd039c5-9755-47d1-b767-659ebec9e8b7.png)



