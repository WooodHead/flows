CREATE TABLE ticket_task (
    id BIGSERIAL PRIMARY KEY,
    task_id VARCHAR(36) NOT NULL UNIQUE,
    customer_agent_config_id VARCHAR(36) NOT NULL,
    conversation_id VARCHAR(64) NOT NULL,
    customer_user_id VARCHAR(255),
    workspace_id VARCHAR(36),
    channel VARCHAR(100),
    task_type VARCHAR(64) NOT NULL,
    status VARCHAR(32) NOT NULL DEFAULT 'PENDING',
    priority INTEGER NOT NULL DEFAULT 3,
    payload JSONB,
    config_snapshot JSONB,
    queue VARCHAR(100),
    retry_count INTEGER NOT NULL DEFAULT 0,
    max_retries INTEGER NOT NULL DEFAULT 0,
    next_run_at TIMESTAMP WITH TIME ZONE,
    last_error VARCHAR(2000),
    result JSONB,
    forward_group_type VARCHAR(64),
    forward_group_name VARCHAR(128),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    deleted BOOLEAN NOT NULL DEFAULT FALSE
);

COMMENT ON TABLE ticket_task IS '工单任务表';

CREATE UNIQUE INDEX idx_ticket_task_task_id ON ticket_task (task_id);
CREATE INDEX idx_ticket_task_conversation ON ticket_task (conversation_id);
CREATE INDEX idx_ticket_task_type ON ticket_task (task_type);
CREATE INDEX idx_ticket_task_status ON ticket_task (status);
CREATE INDEX idx_ticket_task_deleted ON ticket_task (deleted);
