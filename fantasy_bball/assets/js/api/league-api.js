import axios from 'axios';

export function getLeagues() {
  return axios.get('http://localhost:8001/api/v1/leagues/?format=json')
    .then(response => response.data);
}

export function deleteLeague(leagueId) {
  return axios.delete('http://localhost:8001/api/v1/leagues/' + LeagueId);
}

export function getLeague(leagueId) {

  let league = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v1/leagues/' + leagueId + '/?format=json')
    .then(response => {

      let league = response.data;
      league.name = league.name;
      league.manager_id = league.manager;
      league.is_public = league.is_public;
      league.teams = league.teams;

      return league;
      
    });
}