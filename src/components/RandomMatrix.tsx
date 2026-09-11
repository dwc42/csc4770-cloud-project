import { useState } from "react";
import Matrix from "./Matrix";

export default function RandomMatrix() {
	const [nRowSize, setNRowSize] = useState<number>();
	const [mRowSize, setMRowSize] = useState<number>();
	const [matrix, setMatrix] = useState<number[][]>([]);
	return <div>
		n Rows Size
		<input type="number" onChange={(event) => {
			setNRowSize(Number(event.target.value));
		}} />
		n Cols Size
		<input type="number" onChange={(event) => {
			setMRowSize(Number(event.target.value));
		}} />
		<button onClick={() => {

			const newMatrix = Array.from(Array(nRowSize), (_, n) => Array.from(Array(mRowSize), (_, m) => Math.floor(Math.random() * 10)));
			setMatrix(newMatrix);
		}}>Randomize Matrix</button>

		<Matrix matrix={matrix} />
	</div >;
}