

SELECT c.role_name,c.conversation_id,v.user_id,to_char(min(c.created_at), 'YYYY-MM-DD') as created_date
FROM chat_record c,chat_conversation v

WHERE c.conversation_id=v.conversation_id and
( c.equipment_information_id  ='746cde3056fb4d7c8d23b69868c67a9b' 
or c.equipment_information_id  = '4d4c0b69800b476482f7f49157e51ef4'
or c.equipment_information_id  = '08c172f4043d498a9bae48d97fe7ffaf'
or c.equipment_information_id  = '542ef24b817342479b8a6e6459b533aa'
or c.equipment_information_id  = 'eaf82f115e124e09b1b15fc11588c9d9'
or c.equipment_information_id  = '561ed5afab3a4fe5b73b88d4566a7198'
)
and context->>'text' LIKE '%非常感谢亲的支持%'
group by c.equipment_information_id,c.conversation_id,c.role_name,v.conversation_id,v.user_id
order by c.equipment_information_id, min(c.created_at);

