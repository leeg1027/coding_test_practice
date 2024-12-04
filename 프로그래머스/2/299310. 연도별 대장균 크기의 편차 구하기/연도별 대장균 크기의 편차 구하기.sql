select year(DIFFERENTIATION_DATE) YEAR, (b.mx_size-SIZE_OF_COLONY)YEAR_DEV, ID
from(
    select *, year(DIFFERENTIATION_DATE) YEAR
    from ECOLI_DATA) a
join(
    select year(DIFFERENTIATION_DATE) year, max(SIZE_OF_COLONY) mx_size
    from ECOLI_DATA
    group by year) b
on  a.year = b.year
order by YEAR ASC, YEAR_DEV ASC