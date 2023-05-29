-- Создал студент 305 группы Филиппов Владимир

DO $$
DECLARE
    city_table_name text;
    city_id integer;
    measurement_date date;
    measurement_temperature double precision;
BEGIN
    -- ВЫполнение цикла по таблицам во внешней схеме
    FOR city_table_name IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'external'
    LOOP
        -- Проверка, существует ли имя таблицы в поле dataset таблицы city в схеме данных
        EXECUTE format('SELECT id FROM data.city WHERE dataset = %L', city_table_name) INTO city_id;
        
        -- Если соответствующий город найден, вставка измерения в таблицу измерений схемы данных
        IF city_id IS NOT NULL THEN
        
            -- Получение данных измерений из текущей таблицы во внешней схеме
            EXECUTE format('SELECT month, day, year, temperature FROM external.%I', city_table_name)
            INTO measurement_date, measurement_temperature;
            
            -- Вставка результатов измерения в таблицу измерений схем данных
            EXECUTE format('INSERT INTO data.measurement (city, mark, temperature) VALUES (%s, %L, %s)',
                           city_id, measurement_date, measurement_temperature);
        END IF;
        
    END LOOP;
END $$;