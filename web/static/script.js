"use strict";

var search = instantsearch({
  appId: 'HW2AAJ36CM',
  apiKey: 'e18846063dc06b794289ebe4debeaba4',
  indexName: 'mylesb.ca-gifs',
  urlSync: true,
  searchParameters: {
    hitsPerPage: 10
  }
});
search.addWidget(instantsearch.widgets.searchBox({
  container: '#search-input'
}));
search.addWidget(instantsearch.widgets.hits({
  container: '#hits',
  templates: {
    item: document.getElementById('hit-template').innerHTML,
    empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
  }
}));
search.start();
//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImluZGV4LmpzIl0sIm5hbWVzIjpbInNlYXJjaCIsImluc3RhbnRzZWFyY2giLCJhcHBJZCIsImFwaUtleSIsImluZGV4TmFtZSIsInVybFN5bmMiLCJzZWFyY2hQYXJhbWV0ZXJzIiwiaGl0c1BlclBhZ2UiLCJhZGRXaWRnZXQiLCJ3aWRnZXRzIiwic2VhcmNoQm94IiwiY29udGFpbmVyIiwiaGl0cyIsInRlbXBsYXRlcyIsIml0ZW0iLCJkb2N1bWVudCIsImdldEVsZW1lbnRCeUlkIiwiaW5uZXJIVE1MIiwiZW1wdHkiLCJzdGFydCJdLCJtYXBwaW5ncyI6Ijs7QUFBQSxJQUFJQSxNQUFNLEdBQUdDLGFBQWEsQ0FBQztBQUN6QkMsRUFBQUEsS0FBSyxFQUFFLFlBRGtCO0FBRXpCQyxFQUFBQSxNQUFNLEVBQUUsa0NBRmlCO0FBR3pCQyxFQUFBQSxTQUFTLEVBQUUsZ0JBSGM7QUFJekJDLEVBQUFBLE9BQU8sRUFBRSxJQUpnQjtBQUt6QkMsRUFBQUEsZ0JBQWdCLEVBQUU7QUFDaEJDLElBQUFBLFdBQVcsRUFBRTtBQURHO0FBTE8sQ0FBRCxDQUExQjtBQVVBUCxNQUFNLENBQUNRLFNBQVAsQ0FDRVAsYUFBYSxDQUFDUSxPQUFkLENBQXNCQyxTQUF0QixDQUFnQztBQUM5QkMsRUFBQUEsU0FBUyxFQUFFO0FBRG1CLENBQWhDLENBREY7QUFNQVgsTUFBTSxDQUFDUSxTQUFQLENBQ0VQLGFBQWEsQ0FBQ1EsT0FBZCxDQUFzQkcsSUFBdEIsQ0FBMkI7QUFDekJELEVBQUFBLFNBQVMsRUFBRSxPQURjO0FBRXpCRSxFQUFBQSxTQUFTLEVBQUU7QUFDVEMsSUFBQUEsSUFBSSxFQUFFQyxRQUFRLENBQUNDLGNBQVQsQ0FBd0IsY0FBeEIsRUFBd0NDLFNBRHJDO0FBRVRDLElBQUFBLEtBQUssRUFBRTtBQUZFO0FBRmMsQ0FBM0IsQ0FERjtBQVVBbEIsTUFBTSxDQUFDbUIsS0FBUCIsInNvdXJjZXNDb250ZW50IjpbInZhciBzZWFyY2ggPSBpbnN0YW50c2VhcmNoKHtcbiAgYXBwSWQ6ICdIVzJBQUozNkNNJyxcbiAgYXBpS2V5OiAnZTE4ODQ2MDYzZGMwNmI3OTQyODllYmU0ZGViZWFiYTQnLFxuICBpbmRleE5hbWU6ICdteWxlc2IuY2EtZ2lmcycsXG4gIHVybFN5bmM6IHRydWUsXG4gIHNlYXJjaFBhcmFtZXRlcnM6IHtcbiAgICBoaXRzUGVyUGFnZTogMTBcbiAgfVxufSk7XG5cbnNlYXJjaC5hZGRXaWRnZXQoXG4gIGluc3RhbnRzZWFyY2gud2lkZ2V0cy5zZWFyY2hCb3goe1xuICAgIGNvbnRhaW5lcjogJyNzZWFyY2gtaW5wdXQnXG4gIH0pXG4pO1xuXG5zZWFyY2guYWRkV2lkZ2V0KFxuICBpbnN0YW50c2VhcmNoLndpZGdldHMuaGl0cyh7XG4gICAgY29udGFpbmVyOiAnI2hpdHMnLFxuICAgIHRlbXBsYXRlczoge1xuICAgICAgaXRlbTogZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2hpdC10ZW1wbGF0ZScpLmlubmVySFRNTCxcbiAgICAgIGVtcHR5OiBcIldlIGRpZG4ndCBmaW5kIGFueSByZXN1bHRzIGZvciB0aGUgc2VhcmNoIDxlbT5cXFwie3txdWVyeX19XFxcIjwvZW0+XCJcbiAgICB9XG4gIH0pXG4pO1xuXG5zZWFyY2guc3RhcnQoKTtcbiJdLCJmaWxlIjoiaW5kZXguanMifQ==
