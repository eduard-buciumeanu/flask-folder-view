from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert, select
from database.models import engine, Folder, session


from utils.paths import database_path

app = Flask(__name__)
app.secret_key = 'nosecrets'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        folder_name = request.form['FolderNameInput']
        folder_path = request.form['FolderPathInput']

        if folder_name and folder_path:

            try:
                name = str(folder_name)
                path = str(folder_path)

                with session.begin():
                    # insertIntoDB(session, name, path)
                    session.execute(
                        insert(Folder),
                        [
                            {'folder_name': name, 'folder_path': path}
                        ],
                    )

                flash(f'Folder: {name} with path: {path} added!', 'info')
                print(f'Folder name: {folder_name}, folder path: {folder_path}')
            
            except SQLAlchemyError as e:
                flash(f'Folder: {folder_name} with path: {folder_path} raised the following exception: {e}', 'error')
                print(f'Insert failed with error: {e}')
                session.rollback()

            finally:
                return redirect(url_for('home'))
              
        else:

            flash(f'Name and path cannot be empty!', 'warning')

    else:
        return render_template('home.html')


@app.route('/view')
def view():

    folders_table = []

    try:
        with session.begin():
            result = session.execute(select(Folder))
    except SQLAlchemyError as e:
        flash(f'Error: {e}')

    if result:
        for row in result.scalars():

            item = {'folder_name': row.folder_name, 'folder_path': row.folder_path}
            folders_table.append(item)

            # print(f'{row.folder_name} {row.folder_path}')
        
    print(f'Folders table {folders_table}')

    return render_template('view.html', folders_table=folders_table)


if __name__ == '__main__':
    app.run(debug=True)
