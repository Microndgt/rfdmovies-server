from invoke import Collection

import invtasks
from config import basedir

namespace = Collection()
namespace.configure({
    'project_root': basedir
})

namespace.add_collection(Collection.from_module(invtasks, name="web"))
