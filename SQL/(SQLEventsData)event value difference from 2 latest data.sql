select distinct on (event_type) event_type, result * -1
from (select event_type, value, lead(value) over (order by event_type) - value result
      from (select *
            from events
            where event_type in (select event_type
                                 from events
                                 group by event_type
                                 having count(event_type) >= 2)
            order by event_type, time desc) a) b