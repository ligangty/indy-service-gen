INDEX_HTML_TEMPLATE="""<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>$Your Service Name</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/wingcss/0.1.8/wing.min.css"/>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script type="text/javascript">
      <!--
      axios.get('/api/stats/version-info').then(resp => {
        stats = resp.data;
        stats_version=document.getElementById("stats-ver");
        stats_version.innerHTML=stats.version;
        stats_cid=document.getElementById("stats-cid");
        stats_cid.setAttribute("href", `http://github.com/commonjava/{{ service.repo_name }}/commit/${stats['commit-id']}`);
        stats_cid.innerHTML=stats['commit-id'];
        stats_author=document.getElementById("stats-author");
        stats_author.innerHTML=`on ${stats['timestamp']} by ${stats["builder"]}`;
      });
      -->
    </script>
</head>
<body>
<div class="container">
    <h1>$Your Service Name</h1>
    <hr/>


    <div class="cards">
        <div class="card">
            <h5 class="card-header">About</h5>
            <p class="card-body"><b>$Your Service Name</b> provides both REST endpoints manage indy repositories, including creation, changing, deletion and so on.</p>
        </div>

        <div class="card">
            <h5 class="card-header">About APIs</h5>
            <p class="card-body">Check <a href="/q/swagger-ui">swagger-ui</a> for APIs of the service</p>
        </div>


    </div>

    <div id="prj-stats" style="position: fixed; bottom: 5%; text-align: center;">
        <span><a target="_new" class="fa fa-btn" href="http://github.com/Commonjava/{{ service.repo_name }}/issues">Issues</a></span>
        | <span>Version:</span> <span id="stats-ver"></span>
        | <span>Commit ID:</span> <span><a id="stats-cid" target="_new" class="fa fa-btn" href="">{{ '{{stats["commit-id"]}}' }}</a></span>
        | <span>Built</span> <span id="stats-author">on {{ '{{stats["timestamp"]}}' }} by </span>
    </div>

</div>

</body>
</html>
"""