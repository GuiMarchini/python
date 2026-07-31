from config import conectar
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


def criar_usuario(nome, email, senha):
    conn = conectar()
    try:
        conn.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, generate_password_hash(senha))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def verificar_login(email, senha):
    conn = conectar()
    usuario = conn.execute(
        "SELECT * FROM usuarios WHERE email = ?", (email,)
    ).fetchone()
    conn.close()

    if usuario and check_password_hash(usuario["senha"], senha):
        return usuario
    return None


def buscar_tarefas_usuario(usuario_id, ordenar_por="id DESC"):
    conn = conectar()
    tarefas = conn.execute(
        f"SELECT * FROM tarefas WHERE usuario_id = ? ORDER BY {ordenar_por}",
        (usuario_id,)
    ).fetchall()
    conn.close()
    return tarefas


def criar_tarefa(titulo, descricao, status, usuario_id):
    conn = conectar()
    conn.execute(
        """INSERT INTO tarefas
           (titulo, descricao, status, usuario_id)
           VALUES (?, ?, ?, ?)""",
        (titulo, descricao, status, usuario_id)
    )
    conn.commit()
    conn.close()


def buscar_tarefa_por_id(tarefa_id, usuario_id):
    conn = conectar()
    tarefa = conn.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?",
        (tarefa_id, usuario_id)
    ).fetchone()
    conn.close()
    return tarefa


def atualizar_tarefa(tarefa_id, usuario_id, titulo, descricao, status):
    conn = conectar()
    conn.execute(
        """UPDATE tarefas
           SET titulo = ?, descricao = ?, status = ?
           WHERE id = ? AND usuario_id = ?""",
        (titulo, descricao, status, tarefa_id, usuario_id)
    )
    conn.commit()
    conn.close()


def excluir_tarefa(tarefa_id, usuario_id):
    conn = conectar()
    conn.execute(
        "DELETE FROM tarefas WHERE id = ? AND usuario_id = ?",
        (tarefa_id, usuario_id)
    )
    conn.commit()
    conn.close()


def concluir_tarefa(tarefa_id, usuario_id):
    conn = conectar()
    conn.execute(
        """UPDATE tarefas
           SET status = 'Concluída'
           WHERE id = ? AND usuario_id = ?""",
        (tarefa_id, usuario_id)
    )
    conn.commit()
    conn.close()


def buscar_progresso(usuario_id):
    conn = conectar()
    totais = conn.execute(
        """SELECT status, COUNT(*) AS quantidade
           FROM tarefas
           WHERE usuario_id = ?
           GROUP BY status""",
        (usuario_id,)
    ).fetchall()
    conn.close()

    dados = {
        "Pendente": 0,
        "Em andamento": 0,
        "Concluída": 0
    }

    for item in totais:
        dados[item["status"]] = item["quantidade"]

    return dados


def buscar_tarefas_api(usuario_id, status=None):
    conn = conectar()

    if status in ["Pendente", "Em andamento", "Concluída"]:
        tarefas = conn.execute(
            """SELECT id, titulo, descricao, status
               FROM tarefas
               WHERE usuario_id = ? AND status = ?
               ORDER BY id DESC""",
            (usuario_id, status)
        ).fetchall()
    else:
        tarefas = conn.execute(
            """SELECT id, titulo, descricao, status
               FROM tarefas
               WHERE usuario_id = ?
               ORDER BY id DESC""",
            (usuario_id,)
        ).fetchall()

    conn.close()
    return [dict(tarefa) for tarefa in tarefas]