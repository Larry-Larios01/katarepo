select t.agent_id as agent , count(t.id) amount_tickets, ts.name status 
from ticketit t inner join ticketit_statuses ts on t.status_id  = ts.id 
group by t.agent_id, ts.name
