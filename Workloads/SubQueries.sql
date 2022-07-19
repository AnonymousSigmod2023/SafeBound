select COUNT(*) from users as u, posts as p where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId ;
select COUNT(*) from posts as p, votes as v where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and p.Id=v.PostId ;
select COUNT(*) from posts as p, comments as c where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId ;
select COUNT(*) from postLinks as pl, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.PostId=p.Id ;
select COUNT(*) from postHistory as ph, posts as p where ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and ph.PostId=p.Id ;
select COUNT(*) from votes as v, comments as c, posts as p where c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId ;
select COUNT(*) from postLinks as pl, votes as v, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from postHistory as ph, votes as v, posts as p where p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from postLinks as pl, comments as c, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId ;
select COUNT(*) from postHistory as ph, comments as c, posts as p where c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from postLinks as pl, postHistory as ph, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, votes as v where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and p.Id=v.PostId ;
select COUNT(*) from users as u, posts as p, comments as c where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId ;
select COUNT(*) from users as u, posts as p, postLinks as pl where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId ;
select COUNT(*) from users as u, posts as p, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, votes as v, comments as c where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId ;
select COUNT(*) from posts as p, votes as v, postLinks as pl where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from posts as p, votes as v, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, comments as c, postLinks as pl where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId ;
select COUNT(*) from posts as p, comments as c, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, postLinks as pl, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from votes as v, comments as c, postLinks as pl, posts as p where c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from votes as v, comments as c, postHistory as ph, posts as p where c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from votes as v, postLinks as pl, postHistory as ph, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from comments as c, postLinks as pl, postHistory as ph, posts as p where pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, comments as c where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, postLinks as pl where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, comments as c, postLinks as pl where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId ;
select COUNT(*) from users as u, posts as p, comments as c, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, postLinks as pl, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, votes as v, comments as c, postLinks as pl where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from posts as p, votes as v, comments as c, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, votes as v, postLinks as pl, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, comments as c, postLinks as pl, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from votes as v, comments as c, postLinks as pl, postHistory as ph, posts as p where c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, comments as c, postLinks as pl where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, comments as c, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, postLinks as pl, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, comments as c, postLinks as pl, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from posts as p, votes as v, comments as c, postLinks as pl, postHistory as ph where p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId ;
select COUNT(*) from users as u, posts as p, votes as v, comments as c, postLinks as pl, postHistory as ph where u.DownVotes >= 0 and u.UpVotes >= 0 and p.Score >= -2 and p.CommentCount <= 18 and p.CreationDate >= '2010-07-21 13:50:08'::timestamp and p.CreationDate <= '2014-09-11 00:53:10'::timestamp and u.Id=p.OwnerUserId and ph.CreationDate >= '2010-11-27 03:38:45'::timestamp and p.Id=ph.PostId and c.CreationDate >= '2010-07-26 19:37:03'::timestamp and p.Id=c.PostId and pl.CreationDate <= '2014-08-05 18:27:51'::timestamp and p.Id=pl.PostId and p.Id=v.PostId ;