/* still in progress */

function sortable(section, onUpdate) {
    var dragEl, nextEl, newPos, dragGhost;

    let oldPos = [...section.children].map(item => {
        item.draggable = true
        let pos = document.getElementById(item.id).getBoundingClientRect();
        return pos;
    });

    function _onDragOver(e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';

        var target = e.target;
        if (target && target !== dragEl && target.nodeName == 'DIV') {
            if (target.classList.contains('inside')) {
                e.stopPropagation();
            } else {
                //getBoundinClientRect contains location-info about the element (relative to the viewport)
                var targetPos = target.getBoundingClientRect();
                //checking that dragEl is dragged over half the target y-axis or x-axis. (therefor the .5)
                var next = (e.clientY - targetPos.top) / (targetPos.bottom - targetPos.top) > .5 || (e.clientX - targetPos.left) / (targetPos.right - targetPos.left) > .5;

                section.insertBefore(dragEl, next && target.nextSibling || target);

                /*  console.log("oldPos:" + JSON.stringify(oldPos));
                 console.log("newPos:" + JSON.stringify(newPos)); */
                /* console.log(newPos.top === oldPos.top ? 'They are the same' : 'Not the same'); */
                console.log(oldPos);
            }
        }
    }

    function _onDragEnd(evt) {
        evt.preventDefault();
        newPos = [...section.children].map(child => {
            let pos = document.getElementById(child.id).getBoundingClientRect();
            return pos;
        });
        console.log(newPos);
        dragEl.classList.remove('ghost');
        section.removeEventListener('dragover', _onDragOver, false);
        section.removeEventListener('dragend', _onDragEnd, false);

        nextEl !== dragEl.nextSibling ? onUpdate(dragEl) : false;
    }

    section.addEventListener('dragstart', function (e) {
        dragEl = e.target;
        nextEl = dragEl.nextSibling;
        /* dragGhost = dragEl.cloneNode(true);
        dragGhost.classList.add('hidden-drag-ghost'); */

        /*  document.body.appendChild(dragGhost);
         e.dataTransfer.setDragImage(dragGhost, 0, 0); */

        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('Text', dragEl.textContent);

        section.addEventListener('dragover', _onDragOver, false);
        section.addEventListener('dragend', _onDragEnd, false);

        setTimeout(function () {
            dragEl.classList.add('ghost');
        }, 0)

    });
}

sortable(document.getElementById('list'), function (item) {
    /* console.log(item); */
});

/* The setData() method is used to add an item to the drag data, as shown in the following example.

function dragstart_handler(ev) {
  // Add the drag data
  ev.dataTransfer.setData("text/plain", ev.target.id);
  ev.dataTransfer.setData("text/html", "<p>Example paragraph</p>");
  ev.dataTransfer.setData("text/uri-list", "http://developer.mozilla.org"); */


/* you may succeed this a hacky solution. The native draggability doesn't allow CSS styles like: opacity:0;, visibility:hidden or display:none.
But you can do it using: transform:translateX(-9999px).
I've updated your JSFiddle with the solution. */