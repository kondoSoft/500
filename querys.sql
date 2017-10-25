select 
  p.respuesta, 
  e.nombre 
from 
  mxvscorrupcion_empresa as e 
left join 
  mxvscorrupcion_cuestionario_preguntas as cp on cp.cuestionario_id = e.cuestionario_id 
left join 
  mxvscorrupcion_pregunta as p on p.id = cp.pregunta_id 
left join 
  mxvscorrupcion_catalogo_preguntas as catp on catp.id_reactivo=p.id_pregunta 
where 
  catp.id_reactivo = 'TOT100' 
order by 
  p.respuesta desc;


-- Este seria el query para sacar el ranking por sector
select 
  s.nombre,
  count(1)as cnt, 
  sum((e.tot100))/count(1) as porcentaje 
from 
  mxvscorrupcion_empresa as e 
left join 
  mxvscorrupcion_sectores s on s.id=e.sector_id 
group by 
  s.nombre;


-- El ranking global
select 
  e.nombre,e.tot100 
from 
  mxvscorrupcion_empresa as e 
order by 
  e.tot100 desc;


-- query por país
select 
  p.pais,
  count(1)as cnt, 
  sum((e.tot100))/count(1) as porcentaje 
from 
  mxvscorrupcion_empresa as e 
left join 
  mxvscorrupcion_paises p on p.id=e.pais_id 
group by 
  p.pais desc;
