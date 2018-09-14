import { observable, computed } from "mobx";

export default class BarGraphStore {
    @observable model = null;
    @observable target = null;
    @observable callback = null;

    @computed get finished() {
        this.check();
        return !this.model.some(x => !x.correct);
    }

    constructor(puzzle = "012345678", target = "012345678", callback = null) {
        this.model = puzzle.split("").map((o, i) => {
            return {
                id: o,
                x: i % 3,
                y: parseInt(i / 3),
                highlight: false,
                correct: false,
                hide: o == "0"
            };
        });

        this.target = target;
        this.check();
        this.callback = callback;
    }

    check() {
        this.target.split("").map((o, i) => {
            if (this.model[i].id == o) {
                this.model[i].correct = true;
            } else {
                this.model[i].correct = false;
            }
        });
    }

    adjacent(a, b) {
        return (Math.abs(a.x - b.x) + Math.abs(a.y - b.y)) == 1;
    }

    highlight(a = null) {
        let o = this.model.find(x => x.id == a);
        this.model.map(x => {
            if (!o) {
                x.highlight = false;
                return;
            }

            if (this.adjacent(o, x)) {
                x.highlight = true;
            } else {
                x.highlight = false;
            }
        });
    }

    swap(a, b) {
        let oa = this.model.find(x => x.id == a);
        let ob = this.model.find(x => x.id == b);

        if (this.adjacent(oa, ob)) {
            let ax = oa.x;
            let ay = oa.y;

            oa.x = ob.x;
            oa.y = ob.y;

            ob.x = ax;
            ob.y = ay;

            let ia = this.model.findIndex(x => x.id == a);
            let ib = this.model.findIndex(x => x.id == b);

            this.model[ia] = ob;
            this.model[ib] = oa;

            if (this.callback != null) this.callback(this.model.map((x) => x.id).join(""));
        }
    }


}